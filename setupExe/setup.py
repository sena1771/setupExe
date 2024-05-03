

import socket
import os
import zipfile
import sys
import tkinter as tk
import shutil
from tkinter import ttk
#import shutil


ip_address = "127.0.0.1"
port = "9271"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

version = "0.1.4"

folder_path = 'C:\\Example Archive Folder' #TODO: archive file name
script_directory = os.path.dirname(os.path.abspath(__file__))

zip_path = os.path.join(script_directory,'Example_Archive_Folder.zip')

icon_path = os.path.join(script_directory,'some-icon.ico')

def extract_files():
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
       
    if os.path.exists(zip_path):
        with zipfile.ZipFile(zip_path,'r') as zp:
            total_files = len(zp.namelist())
            progress_bar['maximum'] = total_files
            extracted_count = 0
            
            for file_index, file in enumerate(zp.namelist()):
                    
                    
                    file_path= os.path.join(folder_path,file)
                    directory = os.path.dirname(file_path)
                    #if len(file_path) >= 260 :
                        #for supporting long paths
                        #file_path = r'//?/ '+ file_path
                            #with zp.open(file,'r') as file_data ,open(file_path,'wb') as target_file:
                            #shutil.copyfileobj(file_data, target_file)
                            #extracted_count += 1
                   
                    
                    if not os.path.exists(directory):
                        
                        os.makedirs(directory)
                        current_file_label.config(text=f"New directory created : {directory}")


                    if len(file_path) >= 260 :
                        file_path = r'\\?\ ' + file_path
                    try :
                        
                        with zp.open(file) as file_data, open(file_path, 'wb') as output_file:
                            
                            shutil.copyfileobj(file_data,output_file)
                            extracted_count += 1
                            
                    except Exception as ex:
                            current_file_label.config(text =f"Failed to extract {file}: {ex}")
                       
                      
                    #if not os.path.exists(file_path) or os.path.getsize(file_path)!= zp.getinfo(file).file_size:
                         #print("3")
                         #zp.extract(file,folder_path)
                        
                       
                     
                    current_file_label.config(text=f"Extracting : {file}")
                    
                    progress_bar['value'] = file_index + 1
                    
                    root.update_idletasks()
                   

            info_text = f" {extracted_count} files downloaded or updated."     
                    
        #info_label.config(text="New version downloaded successfully.")
        info_label.config(state ='normal')
        info_label.delete(1.0,tk.END)
        info_label.insert(tk.END, "New version downloaded successfully.")
        info_label.config(state = 'disabled')
            #print("Extraction completed")
        download_button.pack_forget()
        progress_bar.pack_forget()
        current_file_label.pack_forget()
        ok_button.pack(side=tk.LEFT, padx=20, pady=20) 
        cancel_button.pack_forget()
    else:
         #print("IPP Tool Archive is not found")
         info_label.config(state = 'normal')
         info_label.delete(1.0,tk.END)
         #info_label.config(text="Download operation is failed")
         info_label.insert(tk.END, "Download failed")
         info_label.config(state = 'disabled')
         download_button.pack_forget()
         progress_bar.pack_forget()
         current_file_label.pack_forget()

def download_and_update():
    download_button.pack_forget()
    progress_bar['value'] = 0
    progress_bar.pack(side= tk.TOP, fill = tk.X, padx=20, pady=5)
    current_file_label.pack(side = tk.TOP, fill = tk.X, padx = 20)
    root.after(100,extract_files)
def close_screen():
    root.destroy()

  
root= tk.Tk()
root.iconbitmap(icon_path)
root.eval('tk::PlaceWindow . center') #centers window
root.geometry('450x300')
root.title("IPP Platform Configuration Tool")
info_text = "IPP Platform Configuration Tool --- Version:" +version+" "+"will be downloaded.\nNew Updates;\n-DTN Interrack Switch Configuration\n-HSN Configuration\n-Report File Creation"
info_label = tk.Text(root,height= 10, width = 50)
info_label.insert(tk.END, info_text)
info_label.pack(pady=10,padx=10)
info_label.config(state = 'disabled')

current_file_label = tk.Label(root,text = "Waiting to start...", anchor ="w")
frame_buttons = tk.Frame(root)
frame_buttons.pack(side = tk.BOTTOM, fill = tk.X)

download_button = tk.Button(frame_buttons,text ="Download/Update", command= download_and_update)
download_button.pack(side=tk.RIGHT,padx=20, pady=20)

cancel_button = tk.Button(frame_buttons,text= "Cancel", command = close_screen)
cancel_button.pack(side=tk.LEFT,padx =20,pady=20)


ok_button = tk.Button(frame_buttons, text="OK", command=close_screen) 

progress_bar = ttk.Progressbar(root,orient='horizontal', mode= 'determinate', length=300)

root.mainloop()




