import re
import pandas as pd

### EXTRACT DATA

with open('CIS_Benchmark_Windows_Server.txt', encoding='utf-8') as f:
    content = f.read()
    # Extract table of content and unneccessary information
    spliter = re.findall("""1.1 Password Policy  

This section contains recommendations for password policy.""", content)
    filtered_content = content.split(spliter[0])
    new_filtered_content = filtered_content[1].split("Appendix: Recommendation Summary")

    # Extract all Criteria
    criteria = re.findall(r'\(L1\)([\s\S]*?)(\(Automated\)|\(Manual\))', new_filtered_content[0], flags=re.MULTILINE)
    list_criteria = []
    for i in criteria[:50]:
        i = f'{i[0]}{i[1]}'
        i = i.replace("\n", " ")
        list_criteria.append(i)
    criteria = list_criteria[:50]

    # Extract all Description
    description = re.findall(r'^Description:\s([\s\S]*?)(?=Note:|Rationale:)', new_filtered_content[0],flags=re.MULTILINE)
    description = [i.strip() for i in description][:50]


    # Extract all Remediation
    remediation = re.findall(r'^Remediation:\s([\s\S]*?)(?=Default Value:)', new_filtered_content[0],flags=re.MULTILINE)
    remediation = [i.strip() for i in remediation][:50]



### WRITE DATA TO EXCEL FILE

# Load the CSV file into a DataFrame
file_path = 'CIS_Benchmark.csv'
df = pd.read_csv(file_path)

# Write data to cell A2 (first row, second column)
k = 0
for i in range(50):
    df.at[k, 'Criteria'] = criteria[i]
    df.at[k, 'Description'] = description[i]
    df.at[k, 'Rememdiation'] = remediation[i]
    k += 1
print(df)
df.to_csv(file_path, index=False)
