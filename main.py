import os
import glob
import json
import pandas as pd
import util

def convert_excel_to_json(excel_file_path: str, output_path: str):
    print("Convert Excel File - " + excel_file_path)

    output_folder_name = os.path.splitext(os.path.basename(excel_file_path))[0]
    output_folder_path = util.create_directory(os.path.join(output_path, output_folder_name))

    try:
        # 엑셀 파일에서 모든 시트 읽기
        xls = pd.ExcelFile(excel_file_path)

        for sheet_name in xls.sheet_names:
            df = pd.read_excel(excel_file_path, sheet_name=sheet_name, header=0)
            json_data = df.to_dict(orient='records')

            # 시트명을 포함한 파일명 설정
            output_file = os.path.join(output_folder_path, f"{sheet_name}.json")

            # JSON 데이터를 파일로 저장
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, ensure_ascii=False, indent=4)

            print(f"Success - '{sheet_name}', OutPut '{output_file}'")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    table_path = os.path.join(os.getcwd(), 'table')
    output_path = os.path.join(os.getcwd(), 'output')

    util.create_directory(table_path)
    util.create_directory(output_path)

    print("TablePath : " + table_path)
    print("OutPUtPath : " + output_path)

    xlsx_files = glob.glob(os.path.join(table_path, '*.xlsx'))

    for file in xlsx_files:
        convert_excel_to_json(file, output_path)