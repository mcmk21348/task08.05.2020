class User:
    # def error(get_accaunt_balance):
    #     def wrapper(get_account_balance):
    #         try:
    #             raise Exception('No username defined!')
    #         except AttributeError:
    #             print('2')
    #     return wrapper
    
    def error1(change_password):
        def wrapper1(change_password):
            try:
                raise Exception('No password to change!')
            except TypeError:
                print('1')
        return wrapper1




    # @error
    # def get_account_balance():
    #     pass
    

    @error1
    def change_password():
        pass
        


u = User()
# u.get_account_balance()
u.change_password()