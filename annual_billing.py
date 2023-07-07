daily_billing_report = {
    "01/01/2023":100450,
    "15/01/2023":102351,
    "20/01/2023":104351,
    "01/02/2023":107000,
    "15/04/2023":108450,
    "15/06/2023":98305,
    "15/08/2023":307480,
    "20/10/2023":103482,
    "01/12/2023":107358,
    "20/12/2023":235482
}

def return_report(daily_billing_report:dict) -> dict:
    max_value = list(daily_billing_report.items())[0][1]
    min_value = list(daily_billing_report.items())[0][1]
    sum_values = 0

    for date in daily_billing_report:
        value = daily_billing_report[date]
        sum_values += value
        max_value = (value if value > max_value else max_value)
        min_value = (value if value < min_value else min_value)

    average = sum_values/len(daily_billing_report)
    values_greater_than_average = 0
    for date in daily_billing_report:
        value = daily_billing_report[date]
        values_greater_than_average += (1 if value > average else 0)

    return{
        "max_value":max_value,
        "min_value":min_value,
        "average":average,
        "values_greater_than_average":values_greater_than_average
        }

print(return_report(daily_billing_report))