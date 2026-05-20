from core.data_profiler import profile_data
from agents.intent_parser import parse_intent
from core.planner import plan_charts
from core.chart_generator import generate_charts
from agents.insight_generator import generate_insights

def run_pipeline(df, user_prompt):
    schema = profile_data(df)
    intent = parse_intent(schema, user_prompt)
    plan = plan_charts(intent, schema)

    charts = generate_charts(df, plan)
    insights = generate_insights(df, plan)

    kpis = {k: "computed_value" for k in intent["kpis"]}

    return {
        "kpis": kpis,
        "charts": charts,
        "insights": insights
    }
