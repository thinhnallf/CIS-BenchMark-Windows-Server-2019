
CIS-BENCHMARK
------
#### This is the CIS-Benchmark for Window Server 2019.
#### This only assesses 50 criteria in Group Policy(Account Policies and Local POlicies)

To export the Group Policy settings, use this PowerShell command: Get-GPOReport -All -ReportType Html -Path "C:\Path\To\exportPolicy.html"

## File explanation: 
- The `CIS_Benchmark_Windows	_Server.txt` is achieved from https://www.cisecurity.org/benchmark/microsoft_windows_server. The file is turned to `.txt` extension for easier manipulation
- First, the `script.py` script will extract all necessary information such as **Criteria**, **Descriptions** and **Remediations**.  After that, it will write these information to an excel file named `CIS-Benchmark.csv`.
- Next, the `policy_extracted_from_windows_sever.py` will extract all criteria and their values from the `policy_extracted.txt` file.
- The process of evaluate these criteria to check whether it pass the requirement or not will be done manually.
