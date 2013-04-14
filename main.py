#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Dan
#
# Created:     08/10/2012
# Copyright:   (c) Dan 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import webapp2
import cgi
form="""
 <!DOCTYPE html>

<html>
  <head>
    <title>Unit 2 Rot 13</title>
  </head>

  <body>
    <h2>Enter some text to ROT13:</h2>
    <form method="post">
      <textarea name="text"
                style="height: 100px; width: 400px;">%(text)s</textarea>
      <br>
      <input type="submit">
    </form>
  </body>

</html>

"""

def rot13(s):
    a=''
    rot13=s.encode('rot13')
    return a
def escape_html(s):
    return cgi.escape(s,quote=True)


class MainPage(webapp2.RequestHandler):
    def write_form(self,text=""):
        self.response.out.write(form %{'text':escape_html(text)} )
    def get(self):
        self.write_form()
    def post(self):
        rot13 = ''
        text = self.request.get('text')
        if text:
            rot13 = text.encode('rot13')
        self.write_form(text=rot13)



app = webapp2.WSGIApplication([('/', MainPage)], debug=True)




