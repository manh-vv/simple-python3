from excel_tool.data_processor import map_customer_code_name, set_sup_name, group_by_sup_name, export_out1, export_incentive
from excel_tool.excel_mongo_tool import worker_excel_mongodb
from excel_tool.variables import data_input


if __name__ == '__main__':
    print("Hello from python")

    # change data input for new input
    worker_excel_mongodb(data_input)

    map_customer_code_name()
    set_sup_name()
    group_by_sup_name()

    # export function
    export_out1(data_input['current_month'])

    if data_input['enable_export_incentive']:
        export_incentive()
    print("===== DONE =====")
