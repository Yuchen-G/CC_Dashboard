import altair as alt
from altair import datum
import pandas as pd
import argparse
alt.renderers.enable('svg')


# Utitlities to create Bars and Text viz for cost_burden metrics 
def createBars(df, cols, county, labelTitle, tooltipTitle, col_sort_order):
    metricCol1 = cols[0]
    metricCol2 = cols[1]
    groupbyCol = cols[1:3]
    valueCol = cols[3]
    bars = alt.Chart(df
            ).transform_joinaggregate(
                total=f'sum({valueCol})',
                groupby=[f'{groupbyCol[0]}', f'{groupbyCol[1]}']
            ).transform_calculate(
                pct = alt.datum.value / alt.datum.total
            ).mark_bar().encode(
                x=alt.X('pct:Q', stack='zero',
                        axis=alt.Axis(format='%', title='', ticks=False)),
                y=alt.Y(f'{metricCol2}:N', axis=alt.Axis(title=''), sort=col_sort_order),
                color=alt.Color(f'{metricCol1}:N',
                    scale=alt.Scale(domain=cost_burden_display, range=range_),
                    legend=alt.Legend(orient='none', direction='horizontal',
                    legendX=-50, legendY=-30, title=f'{labelTitle}', 
                    titleAnchor='middle', titleFontSize=15)),
                order=alt.Order('cost_burden_index:Q', sort='ascending'),
                tooltip=[
                        alt.Tooltip(f'{metricCol1}:N'),
                        alt.Tooltip(f'{valueCol}:Q', title=f'{tooltipTitle}'),
                        alt.Tooltip('pct:Q', title='Percent', format='0.0%')                    
                      ]
      ).transform_filter(datum.variable == f'{county}') 
    return(bars)

def createText(df, cols, county, labelTitle, col_sort_order):
        metricCol1 = cols[0]
        metricCol2 = cols[1]
        groupbyCol = cols[1:3]
        valueCol = cols[3]  
        text = alt.Chart(df
                ).transform_joinaggregate(
                      total=f'sum({valueCol})',
                      groupby=[f'{groupbyCol[0]}', f'{groupbyCol[1]}']
                ).transform_calculate(
                      pct = alt.datum.value / alt.datum.total
                ).mark_text(dx=-10, dy=3, color='white').encode(
                            x=alt.X('pct:Q', stack='zero',
                                    axis=alt.Axis(format='.1%', title='', ticks=False)),
                            y=alt.Y(f'{metricCol2}:N', axis=alt.Axis(title=''), sort=col_sort_order),
                            text=alt.Text('pct:Q', format='.0%'),
                            detail='pct:Q',
                            order=alt.Order('cost_burden_index:Q',
                                            sort='ascending')
                ).transform_filter(datum.variable == f'{county}')
        return(text)
    
cost_burden_display = ['Severly Cost Burdened (50% or more)', 'Cost Burdened (30% or more, but less than 50%)','Unburdened (Less than 30%)']
household_incomes_ord = ['Extremely Low Income (0-30% AMI)', 'Very Low Income (31-50% AMI)',  \
                             'Low Income (51-80% AMI)', '80+% AMI']
cost_burden_ord = ['Severly Cost Burdened (50% or more)', 'Cost Burdened (30% or more, but less than 50%)','Unburdened (Less than 30%)']  
range_ = ['#7e537f','#e4891e', '#eab676']

tenure_ord = ['Renter', 'Owner', 'Total']
labelTitle = 'Level of Cost Burden'
tooltipTitle = 'Cost Burdened Households'


if __name__ == '__main__':    
    parser = argparse.ArgumentParser()
    parser.add_argument('ASSETS_PATH', help='input path for datasets')
    parser.add_argument('COUNTY', help='GrossRent by BedRooms file (json)')
    parser.add_argument('COST_BURDEN_INCOME', help='GrossRent by BedRooms file (json)')
    parser.add_argument('COST_BURDEN_TENURE', help='GrossRent by BedRooms file (json)')    
    parser.add_argument('COST_BURDEN_INCOME_IMG', help='GrossRent by BedRooms file (json)')
    parser.add_argument('COST_BURDEN_TENURE_IMG', help='GrossRent by BedRooms file (json)')    

    
    args = parser.parse_args()    
        
    cost_burden_income_df = pd.read_csv(args.ASSETS_PATH + args.COST_BURDEN_INCOME)
    income_cols = list(cost_burden_income_df.columns)
    county = args.COUNTY
    
    bars = createBars(cost_burden_income_df, income_cols, county, labelTitle, tooltipTitle, household_incomes_ord)
    text = createText(cost_burden_income_df, income_cols, county, labelTitle, household_incomes_ord)

    income_chart = (bars + text
                     ).properties(width=600, height=400, title={"text" : 'Cost Burden By Income - ' + f'{county} (2014-2018)',
                                              "subtitle" : 'Percent of Households',
                                              "fontSize": 25,
                                              "subtitleFontSize":20,
                                              "anchor":"start"}
                    ).configure_view(strokeWidth=0
                    ).configure_axis(labelFontSize=15, 
                                     grid=False, domain=False)  
    
    income_chart.save(args.ASSETS_PATH + args.COST_BURDEN_INCOME_IMG, embed_options={'renderer':'svg'})
    
    
    cost_burden_tenure_df = pd.read_csv(args.ASSETS_PATH + args.COST_BURDEN_TENURE)
    tenure_cols = list(cost_burden_tenure_df.columns)

    bars = createBars(cost_burden_tenure_df, tenure_cols, county, labelTitle, tooltipTitle, tenure_ord)
    text = createText(cost_burden_tenure_df, tenure_cols, county, labelTitle, tenure_ord)

    tenure_chart = (bars + text
                     ).properties(width=600, height=400, title={"text" : 'Cost Burden By Tenure - ' +f'{county} (2014-2018)',
                                              "subtitle" : 'Percent of Households',
                                              "fontSize": 25,
                                              "subtitleFontSize":20,
                                              "anchor":"start"}
                    ).configure_view(strokeWidth=0
                    ).configure_axis(labelFontSize=15, 
                                     grid=False, domain=False)
    
    tenure_chart.save(args.ASSETS_PATH + args.COST_BURDEN_TENURE_IMG, embed_options={'renderer':'svg'})