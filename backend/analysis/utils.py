import google.generativeai as genai   # Correct Gemini import

import pandas as pd
import os
from pathlib import Path
import re
from django.conf import settings

# -------------------------------
# Gemini SDK Setup (Correct Way)
# -------------------------------
if settings.GEMINI_API_KEY:
    genai.configure(api_key=settings.GEMINI_API_KEY)
    GEMINI_MODEL = "models/gemini-flash-latest"
    model = genai.GenerativeModel(GEMINI_MODEL)
else:
    model = None
    GEMINI_MODEL = None


BASE_DIR = Path(__file__).resolve().parent.parent
EXCEL_FILE_PATH = BASE_DIR / 'data' / 'sample_data.xlsx'


def load_excel_data():
    if os.path.exists(EXCEL_FILE_PATH):
        return pd.read_excel(EXCEL_FILE_PATH)
    return None



def extract_areas_from_query(query):
    """Extract area names from user query"""
    df = load_excel_data()
    if df is None:
        return []
    
    query_lower = query.lower()
    all_areas = df['final location'].unique()
    
    found_areas = []
    for area in all_areas:
        if area.lower() in query_lower:
            found_areas.append(area)
    
    return found_areas


def filter_data_by_areas_and_years(areas, years=None):
    """Filter data by areas and optionally by years"""
    df = load_excel_data()
    if df is None:
        return pd.DataFrame()
    
    filtered_df = df[df['final location'].isin(areas)]
    
    if years:
        filtered_df = filtered_df[filtered_df['year'].isin(years)]
    
    return filtered_df


def extract_year_constraint(query):
    """Extract year constraints from query (e.g., 'last 3 years')"""
    df = load_excel_data()
    if df is None:
        return None
    
    query_lower = query.lower()
    
    match = re.search(r'last\s+(\d+)\s+years?', query_lower)
    if match:
        num_years = int(match.group(1))
        max_year = df['year'].max()
        return list(range(max_year - num_years + 1, max_year + 1))
    
    years = re.findall(r'\b(20\d{2})\b', query)
    if years:
        return [int(year) for year in years]
    
    return None


# -------------------------------
# Gemini Summary Generator (Fixed)
# -------------------------------
def generate_summary(query, areas, data):
    if not areas or data.empty:
        return "I couldn't find any data for the specified areas. Please try again with valid area names."

    if model:
        try:
            data_summary = data.to_string(index=False, max_rows=50)

            prompt = f"""
You are a real estate analyst. Analyze the following real estate data and provide insights based on the user's query.

User Query: "{query}"
Areas of Interest: {', '.join(areas)}

Real Estate Data:
{data_summary}

Provide:
1. Clear summary
2. Price trends & demand patterns
3. Comparison if multiple areas are mentioned
4. Actionable insights

Format in clean Markdown.
"""

            response = model.generate_content(prompt)

            return response.text
        
        except Exception as e:
            print("Gemini API Error:", e)
            return "An error occurred while generating summary."

    return "Gemini API not configured. Please add GEMINI_API_KEY in Django settings."


def get_demand_label(score):
    """Get demand label based on score"""
    if score >= 90:
        return "Very High Demand"
    elif score >= 80:
        return "High Demand"
    elif score >= 70:
        return "Moderate Demand"
    else:
        return "Low Demand"


def prepare_chart_data(data, query):
    """Prepare data for chart visualization"""
    query_lower = query.lower()
    
    chart_data = []
    
    for year in sorted(data['year'].unique()):
        year_entry = {'year': int(year)}
        
        for area in data['final location'].unique():
            area_data = data[(data['year'] == year) & (data['final location'] == area)]
            
            if not area_data.empty:
                # Use flat weighted average rate as price indicator
                if 'price' in query_lower or 'rate' in query_lower:
                    year_entry[f"{area}_price"] = float(area_data['flat - weighted average rate'].values[0])
                
                # Use total sold as demand indicator
                if 'demand' in query_lower or 'sold' in query_lower:
                    year_entry[f"{area}_demand"] = int(area_data['total sold - igr'].values[0])
                
                # Use total sales as transaction value
                if 'transaction' in query_lower or 'sales' in query_lower:
                    year_entry[f"{area}_sales"] = float(area_data['total_sales - igr'].values[0])
                
                # Default: show both price and demand
                if ('price' not in query_lower and 'demand' not in query_lower and 
                    'transaction' not in query_lower and 'sales' not in query_lower and
                    'rate' not in query_lower and 'sold' not in query_lower):
                    year_entry[f"{area}_price"] = float(area_data['flat - weighted average rate'].values[0])
                    year_entry[f"{area}_demand"] = int(area_data['total sold - igr'].values[0])
        
        chart_data.append(year_entry)
    
    return chart_data


def prepare_table_data(data):
    """Prepare data for table display"""
    # Select key columns for display
    display_columns = [
        'final location', 'year', 'total sold - igr', 
        'flat - weighted average rate', 'total_sales - igr'
    ]
    
    # Filter to only include columns that exist
    available_columns = [col for col in display_columns if col in data.columns]
    display_data = data[available_columns].copy()
    
    # Calculate derived metrics
    # Avg Size = (Total Sales Value / Price/SqFt) / Total Sold Count
    if all(col in display_data.columns for col in ['total_sales - igr', 'flat - weighted average rate', 'total sold - igr']):
        try:
            display_data['Avg_Size_SqFt'] = (
                display_data['total_sales - igr'] / display_data['flat - weighted average rate']
            ) / display_data['total sold - igr']
            display_data['Avg_Size_SqFt'] = display_data['Avg_Size_SqFt'].round(0)
        except:
            display_data['Avg_Size_SqFt'] = 0
    else:
        display_data['Avg_Size_SqFt'] = 0

    # Demand Score - using Total Sold as a proxy
    if 'total sold - igr' in display_data.columns:
         display_data['Demand_Score'] = display_data['total sold - igr']
    else:
         display_data['Demand_Score'] = 0

    # Rename for better readability matching Frontend DataTable.jsx
    display_data = display_data.rename(columns={
        'final location': 'Area',
        'year': 'Year',
        'flat - weighted average rate': 'Price_Per_SqFt',
        'total sold - igr': 'Transactions'
    })
    
    # Fill NaNs and ensure correct types
    display_data = display_data.fillna(0)
    
    return display_data.to_dict('records')
