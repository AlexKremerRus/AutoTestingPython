data_1 = ['Desktop', 'Notes', 'Commands', 'Documents', 'WorkSpace', 'React', 'Angular', 'Veu', 'Office', 'Public',
          'Private', 'Classified', 'General', 'Word File.doc']
data_2 = ['desktop', 'notes', 'commands', 'documents', 'workspace', 'react', 'angular', 'veu', 'office', 'public',
          'private', 'classified', 'general', 'wordFile']

#print(str(data_1).lower().replace(' ','').replace('.doc',''))

data_1=(str(data_1).lower().replace(' ','').replace('.doc',''))
data_2=str(data_2).lower().replace(' ','')
assert data_1==data_2
