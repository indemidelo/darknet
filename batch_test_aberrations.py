import subprocess


test = ["data/obj/prova1_C_2019-02-06-152723-0050.jpg", 
        "data/obj/prova_1_2019-02-06-152110-0003.jpg"]

with open("data/test_aberrations/test_aberrations.txt", "r") as testfile:
    #for row in test:
    for row in testfile:
        #print(row)
        filename = row.split('\n')[0]
        #print('filename del file', filename)
        #print('filename di prova', test[0].split('/')[-1])
        predname = f"{filename.split('.')[0]}_predictions"
        #print('predname', predname)
        command = ['./darknet', 'detect', 'cfg/yolo-obj.cfg', 
                '../../backup_entrambe/yolo-obj.backup', 
                'data/test_aberrations/{}'.format(filename), '-out', 
                #'/user/github/darknet/data/entrambe/{}'.format(predname)]
                'pred_aberrations/{}'.format(predname)]
        subprocess.call(command)
        continue
        output, error = subprocess.Popen(
                command, universal_newlines=True,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        #subprocess.call("./darknet detect cfg/yolo-obj.cfg ../../backup_entrambe/yolo-obj.backup data/entrambe/data/obj/{} -out /user/github/darknet/data/entrambe/{}".format(filename, predname),
		#shell=True)
