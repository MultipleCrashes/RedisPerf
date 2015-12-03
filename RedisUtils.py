import os 
import redis 
import timeit 

class RedisFunctions:
	
	def __init__(self,host='localhost',port=6379):
		self.host      = host 
		self.port      = port 	
		self.conn_pool = redis.ConnectionPool(host=self.host,port=self.port)
		self.db_handle = redis.Redis(connection_pool=self.conn_pool)


	def _insert_data(self,host='localhost',port=6379):
		for i in range(1,100000):
			k = i+10
			self.db_handle.set(i,k)
			print "Inserting into redis ",i
 
	def _get_data(self,host='localhost',port=6379):
		for i in range(1,100000):
			value = self.db_handle.get(i)	
			print "Value = ",value


	def _performance(self,host='localhost',port=6379):
		print "Performance Metrics " 
		print timeit.Timer('"for i in range(1,100000): print self.db_handle.get(i)"').repeat(5,10)
		


if __name__ == '__main__':
	mod_obj = RedisFunctions()
	mod_obj._insert_data()
	mod_obj._get_data()
	mod_obj._performance()
