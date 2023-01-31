from psycopg2 import errorcodes
import sys

class Error:
    
    @classmethod
    def print_psycopg2_exception(self, err):
        # get details about the exception
        err_type, err_obj, traceback = sys.exc_info()
        
        # get the line number when exception occured
        line_num = traceback.tb_lineno
        
        # print the connect() error
        print ("\npsycopg2 ERROR:", err, "on line number:", line_num)
        print ("psycopg2 traceback:", traceback, "-- type:", err_type)

        # psycopg2 extensions.Diagnostics object attribute
        print ("\nextensions.Diagnostics:", err.diag)

        # print the pgcode and pgerror exceptions
        print ("pgerror:", err.pgerror)
        print ("pgcode:", err.pgcode, "\n")
    
    @classmethod
    def exceptions(self, err):
        # get details about the exception
        err_type, err_obj, traceback = sys.exc_info()
        print('Error type:', err_type, 'PgCode: ', err.pgcode)
        if(err.pgcode == errorcodes.INVALID_DATETIME_FORMAT):
            return "Por favor, insira um valor de data válido! Ex.: 2023-01-28 22:20"