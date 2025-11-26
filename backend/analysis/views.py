from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import (
    extract_areas_from_query,
    extract_year_constraint,
    filter_data_by_areas_and_years,
    generate_summary,
    prepare_chart_data,
    prepare_table_data
)


@api_view(['POST'])
def query_analysis(request):
    """
    Process user query and return analysis with summary, chart data, and table data
    """
    try:
        query = request.data.get('query', '')
        
        if not query:
            return Response(
                {'error': 'Query is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Extract areas from query
        areas = extract_areas_from_query(query)
        
        if not areas:
            return Response({
                'summary': "I couldn't identify any areas in your query. Please mention specific areas like Wakad, Aundh, Akurdi, Ambegaon Budruk, or Hinjewadi.",
                'chart_data': [],
                'table_data': [],
                'areas': []
            })
        
        # Extract year constraints
        years = extract_year_constraint(query)
        
        # Filter data
        filtered_data = filter_data_by_areas_and_years(areas, years)
        
        if filtered_data.empty:
            return Response({
                'summary': f"No data found for {', '.join(areas)} in the specified time period.",
                'chart_data': [],
                'table_data': [],
                'areas': areas
            })
        
        # Generate summary
        summary = generate_summary(query, areas, filtered_data)
        
        # Prepare chart data
        chart_data = prepare_chart_data(filtered_data, query)
        
        # Prepare table data
        table_data = prepare_table_data(filtered_data)
        
        return Response({
            'summary': summary,
            'chart_data': chart_data,
            'table_data': table_data,
            'areas': areas
        })
    
    except Exception as e:
        return Response(
            {'error': f'An error occurred: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def get_available_areas(request):
    """
    Get list of all available areas in the dataset
    """
    try:
        from .utils import load_excel_data
        df = load_excel_data()
        
        if df is None:
            return Response(
                {'error': 'Could not load data'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        areas = sorted(df['final location'].unique().tolist())
        years = sorted(df['year'].unique().tolist())
        
        return Response({
            'areas': areas,
            'years': years
        })
    
    except Exception as e:
        return Response(
            {'error': f'An error occurred: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def health_check(request):
    """Simple health check endpoint"""
    return Response({'status': 'ok', 'message': 'Real Estate Analysis API is running'})
