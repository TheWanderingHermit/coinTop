import request_handler

class info_parser :
    def __init__( self ) :
        self.response_generic_params = [ 'Response', 'Message', 'BaseImageUrl', 'BaseLinkUrl', 'Type' ]
        self.response_data_params    = [ 'Id', 'Url', 'ImageUrl', 'Name', 'CoinName', 'FullName', 'Algorithm', 'ProofType', 'SortOrder' ]
    def parse_coin_list( self, response ) :
        coin_list_info   = response.json()
        coin_key_context = coin_list_info[ 'Data' ]
        return [ x for x in coin_key_context ]
    def parse_coin_price( self, response ) :
        coin_price_info = response.json()
        return [ ( x, coin_price_info[ x ] ) for x in coin_price_info ]
    def parse_coin_prices( self, response ) :
        coin_prices_info = response.json()
        coin_data_frame = []
        for coin in coin_prices_info :
            coin_data = [ coin ]
            for currency in coin_prices_info[ coin ] :
                coin_data.append( coin_prices_info[ coin ][ currency ] )
            coin_data_frame.append( coin_data )
        return coin_data_frame

if __name__ == '__main__' :
    info_handler = request_handler.request_handler()
    data_parser  = info_parser()
    coin_list    = data_parser.parse_coin_list( info_handler.get_coin_list() );
    multi_coin_prices = info_handler.get_multi_coin_price( fsyms=','.join(coin_list[ :10 ]) )
    print( data_parser.parse_coin_prices( multi_coin_prices ) )
