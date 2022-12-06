from __future__ import print_function
import frida
import sys,os,time

SCRIPT_PATH  = "./Scripts"
SCRIPT_NAME = "tool.js"

def BringScript(name):
    global SCRIPT_PATH
    filename = os.path.join(SCRIPT_PATH,name)
    fp = open(filename,"rt")
    content = fp.read()
    fp.close()

    return content
    
def BuildMasterScript():
    global SCRIPT_NAME
    content = "" 
    content = BringScript(SCRIPT_NAME)
    
    return content

def on_message(message,data):
    print(message)


def attachment(PROCESS_NAME):
    i = 0
    flag = 1
    while flag:
        os.system('cls') 
        if i%3 == 0 :
            print("Wainting for Process : "+PROCESS_NAME+"...",end='\r')        
        elif i%3 == 1 :
            print("Wainting for Process : "+PROCESS_NAME+"....",end='\r')
        elif i%3 == 2 :
            print("Wainting for Process : "+PROCESS_NAME+".....",end='\r')
        # session = frida.attach(PROCESS_NAME)
        try :
            session = frida.attach(PROCESS_NAME)
            if session :
                print("\nattach Successsful! : "+PROCESS_NAME)
                script = session.create_script(jscontent)
                script.on('message',on_message)
                script.load()
                sys.stdin.read()
                flag=0
            else :
                print("attach Failed! : "+PROCESS_NAME) 
        except:
            pass
        time.sleep(0.8)
        i = i+1

def spawnProcess(pPath,r):
    pid=frida.spawn(pPath)
    if pid : 
        print("\n[+] process spawn Successsful! : "+str(pid)+"("+hex(pid)+")")
    session = frida.attach(pid)
    if session : 
        print("[+] attach Successsful! : "+pPath)
        script = session.create_script(jscontent)
        if r == 1 : 
            frida.resume(pid)
            print("[-] resumming...")
        script.on('message',on_message)
        script.load()
        sys.stdin.read()
    else :
        print("attach Failed! : "+pPath) 

def errmsg(err):
    if err == 0:
        print("plz input argument \n attach : -a processname \n spawn : -s filepath ResumeOption(0:pause,1:resume)")

jscontent = BuildMasterScript()



print("::::::::: Frida process monitoring tool :::::::::")
if len(sys.argv) < 3:
    errmsg(0)
else :         
    if sys.argv[1] == "-a" : 
        attachment(sys.argv[2])
    elif sys.argv[1] == "-s":
        if len(sys.argv) < 4:
            errmsg(0)
        else :  
            spawnProcess(sys.argv[2],sys.argv[3])
    else: 
        errmsg(0)













