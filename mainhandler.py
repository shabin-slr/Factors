import webapp2

MAIN_PAGE_HTML = """\
<html>
  <body>
    <form action="/sign" method="post">
      <div><input name="num" type="number"></input></div>
      <div><input type="submit" value="Get Factors"></div>
    </form>
  </body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write(MAIN_PAGE_HTML)