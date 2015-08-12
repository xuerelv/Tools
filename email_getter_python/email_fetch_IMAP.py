import imaplib
import email
import base64

def extract_body(payload):
    if isinstance(payload,str):
        return payload
    else:
        return '\n'.join([extract_body(part.get_payload()) for part in payload])

conn = imaplib.IMAP4("nlp.nju.edu.cn", 143)
print conn.state

conn.login_cram_md5('xxx@nlp.nju.edu.cn','xxx')

print conn.state
conn.select('INBOX',False)
typ, data = conn.search(None, 'ALL')

for num in str.split(data[0]):
    try:
        typ, data = conn.fetch(num, '(UID BODY.PEEK[])')
        msg = email.message_from_string(data[0][1])
        filename=str(t)+".eml"
        f=open(filename,'wb')
        f.write(str(msg))
        f.close
    except Exception,e:
        print 'got msg error: %s' % e            
    print "OK!"+str(t)

conn.logout()
#conn.close()
