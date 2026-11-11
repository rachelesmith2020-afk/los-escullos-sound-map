import json,sys
t=open('template.html').read(); b=json.load(open('base.json'))
photos=json.load(open('photos.json')) if len(sys.argv)>1 else {}
audio=json.load(open('audio.json')) if len(sys.argv)>1 else {}
t=t.replace('__W__',f"{b['W']:.0f}").replace('__H__',f"{b['H']:.0f}").replace('__SVG__',b['svg'])
t=t.replace('__SPOTS__',json.dumps(json.load(open('spots.json')),ensure_ascii=False)).replace('__PHOTOS__',json.dumps(photos)).replace('__AUDIO__',json.dumps(audio,ensure_ascii=False))
t=t.replace('__PACK__','https://freesound.org/people/oolita/packs/46523/')
open('los-escullos-sound-map.html','w').write(t); print(len(t))
