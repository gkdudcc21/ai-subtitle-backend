from datetime import datetime

print(datetime.now())

timestamp = datetime.now().strftime('%Y%m%d-%H%M%S') 
print(timestamp)

# file_name = 'subtitlr-' + timestamp + '.srt'
file_name = f'subtitlr- {timestamp} .srt'
print(file_name)