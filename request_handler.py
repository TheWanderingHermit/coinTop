# class that handles coin information requests
import requests

class request_handler :
    def __init__( self, coin_list_url = 'https://www.cryptocompare.com/api/data/coinlist/', coin_price_url = 'https://min-api.cryptocompare.com/data' ) :
        self.coin_list_url  = coin_list_url
        self.coin_price_url = coin_price_url
    def get_coin_list( self ) :
        response = requests.get( url = self.coin_list_url )
        return response
    def get_coin_price( self, fsym = 'ETH', tsyms = 'BTC,USD,EUR', e = 'CCCAGG', extraParams = 'coinTop', sign = False, tryConversion = True ) :
        url_params = { 'fsym' : fsym, 'tsyms' : tsyms, 'e' : e, 'extraParams' : extraParams, 'sign' : sign, 'tryConversion' : tryConversion }
        price_url  = '%s/price' % ( self.coin_price_url )
        response   =  requests.get( url = price_url, params = url_params )
        return response
    def get_multi_coin_price( self, fsyms = 'ETH,DASH', tsyms = 'BTC,USD,EUR', e = 'CCCAGG', extraParams = 'coinTop', sign = False, tryConversion = True ) :
        url_params       = { 'fsyms' : fsyms, 'tsyms' : tsyms, 'e' : e, 'extraParams' : extraParams, 'sign' : sign, 'tryConversion' : tryConversion }
        multi_price_url  = '%s/pricemulti' % ( self.coin_price_url )
        response         = requests.get( url = multi_price_url, params = url_params )
        return response
