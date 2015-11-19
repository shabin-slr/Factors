import cgi
import webapp2
global getfactors

class FormHandler(webapp2.RequestHandler):
	
	#@classmethod	
	def getFactors(self, num):
		num = int(num)
		print "num is : ", num
		
		if num < 0 :
			num *= -1
			
		if ( num == 1 or num == 2):
			return str(num);
		result = []
		i = 2
		while ( i <= num/2 ):
			if( num % i == 0 ):
				result.append(i)
			i+=1
		print result
		return ', '.join(str(n) for n in result)
		
	def post(self):
		self.response.write('<html><body>You wrote:<pre>')
		self.response.write(cgi.escape(self.request.get('num')))
		self.response.write('<p>Factors are:</p><p>')
		self.response.write(self.getFactors(self.request.get('num')))
		#self.getFactors(
		self.response.write('</p></pre></body></html>')