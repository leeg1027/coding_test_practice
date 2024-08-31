def solution(phone_book):
    phone_book = sorted(phone_book, key=len)
    prefixes = {}
    
    for number in phone_book:
        prefix = ''
        for digit in number:
            prefix += digit
            if prefix in prefixes:
                return False
        prefixes[number] = True
        
    return True
