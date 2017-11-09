# https://github.com/discogs/discogs_client
# pip install discogs_client

import discogs_client
import time
import json
d = discogs_client.Client('ExampleApplication/0.1', user_token="*****DISCOGS**USER**TOKEN**HERE*****")

me = d.identity()
co = me.collection_folders[0].releases

VIDS = []

for i in co:
	print '%-22.20s%22.20s' % (i.release.data['title'], i.release.data['artists'][0]['name'])
	vs = i.release.videos
	for v in vs:
		print '%10s%52.50s%52.50s' % ('', v.data['title'], v.data['uri'])
		VIDS.append(v.data['uri'])
	time.sleep(2)

f = open('vidlist.json', 'w')
f.write(json.dumps(VIDS))
f.close()