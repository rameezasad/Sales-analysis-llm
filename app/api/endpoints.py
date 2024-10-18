from fastapi import APIRouter
from app.utils.data_processing import load_sales_data, get_gpt_insights

router = APIRouter()

@router.get("/api/rep_performance")
def rep_performance(rep_id: str):
    sales_data = load_sales_data('sales_performance_data.csv')
    analysis = get_gpt_insights(sales_data.to_string(), f"Analyze the performance of sales representative with ID {rep_id}: ")
    return {"rep_performance": f"Performance for rep {rep_id}"}

@router.get("/api/team_performance")
def team_performance():
    sales_data = load_sales_data('sales_performance_data.csv')
    analysis = get_gpt_insights(sales_data.to_string(), "Analyze the overall team performance.")
    return {"team_performance": analysis}
