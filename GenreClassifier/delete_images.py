''' Deleting images '''
def empty_folder(deletion_path):
    import os
    print('deleting waste')
    print(deletion_path)
    count = 0
    while True:
        try:
            os.remove(deletion_path + "\\frame%d.jpg"%(count))
            count+=1
        except:
            print('No more to delete')
            break
    