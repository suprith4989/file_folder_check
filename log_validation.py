import os

ccsp = [
    'test_name1',
    'test_name2',
    'test_name3',
    'test_name4'
    ]

write_to_file = open('folder_exists', 'w')
write_to_file1 = open('log_file_exists', 'w')
write_to_file2 = open('log_validation', 'w')
length = len(ccsp)
path = '/var/log/<dir_name>/runs/1/cloud/'
path1 = '/var/log/<dir_name>/runs/1/rcert/'
path2 = 'self_check'

def folder_validation(ccsp):
    for i in range(0, length):
        os.chdir(path)
        if os.path.exists(ccsp[i]):
            write_to_file.write('Log folder exists for '+' '+ccsp[i]+'\n')

        else:
            write_to_file.write('Log folder does not exist for '+' '+ccsp[i]+' \n')

def self_check_exists():
    if os.path.exists(path1):
        os.chdir(path1)
        if os.path.exists(path2):
            os.chdir(path2)
            if os.path.exists('output.log') and os.access('output.log', os.R_OK):
                write_to_file1.write('Output Log file exists for '+' '+path2+' and is readable \n')
                data = [line.strip() for line in open('output.log', 'r')]
                if data[-3] == '<summary data-value="FAIL">FAIL</summary>':
                    write_to_file2.write('Log file validation successful for '+path2+' test of CCSP but the final result is Fail \n')
                else:
                    write_to_file2.write('Log file validation successful for '+' '+path2+' test of CCSP and final result is Pass \n')
            else:
                write_to_file1.write('Output Log file does not exist for '+' '+path2+' \n')
        else:
            write_to_file1.write('Test was not run for '+' '+path2+' or the file is not readable \n')
    else:
        write_to_file.write('Test run was not successful')

def logfile_exists(ccsp):
    for i in range(0, length):
        if os.path.exists(path):
            os.chdir(path)
            if os.path.exists(ccsp[i]):
                os.chdir(ccsp[i])
                if os.path.exists('output.log') and os.access('output.log', os.R_OK):
                    write_to_file1.write('Output Log file exists for '+' '+ccsp[i]+' and is readable \n')
                else:
                    write_to_file1.write('Output Log file does not exist for '+' '+ccsp[i]+' \n')
            else:
                write_to_file1.write('Test was not run for '+' '+ccsp[i]+' or the file is not readable \n')
        else:
            write_to_file.write('Test run was not successful')

def logfile_validation(ccsp):
    for i in range(0, length):
        if os.path.exists(path):
            os.chdir(path)
            if os.path.exists(ccsp[i]):
                os.chdir(ccsp[i])
                if os.path.exists('output.log') and os.access('output.log', os.R_OK):
                    write_to_file1.write('Output Log file exists for '+' '+ccsp[i]+' and is readable \n')
                    data = [line.strip() for line in open('output.log', 'r')]
                    if data[-3] == '<summary data-value="FAIL">FAIL</summary>':
                        write_to_file2.write('Log file validation successful for '+ccsp[i]+' test of CCSP but the final result is Fail \n')
                    else:
                        write_to_file2.write('Log file validation successful for '+' '+ccsp[i]+' test of CCSP and final result is Pass \n')
                else:
                    write_to_file1.write('Output Log file does not exist for '+' '+ccsp[i]+' \n')
            else:
                write_to_file1.write('Test was not run for '+' '+ccsp[i]+' or the file is not readable \n')
        else:
            write_to_file.write('Test run was not successful')

folder_validation(ccsp)
logfile_exists(ccsp)
logfile_validation(ccsp)
self_check_exists()
