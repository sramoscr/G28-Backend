class UserResource:
    def create(self, json):
        try:
            return {}
        except Exception as e:
            return {
                'error': str(e)
            }, 500
        
    def list(self):
        try:
            users = []
            with open('users.txt', 'r') as file:
               lines = file.readlines()
               for line in lines:
                   datos = line.strip().split(',')
                   id = int(datos[0])
                   name = datos[1]
                   email=datos[2]
                   age = int(datos[3])
                   users.append({
                       'id': id,
                       'name': name,
                       'email': email,
                       'age': age
                   }) 
            return users
        except Exception as e:
            return {
                'error': str(e)
            }, 500
    
    def update(self, id, json):
        try:
            return {}
        except Exception as e:
            return {
                'error': str(e)
            }, 500
        
    def delete(self, id):
        try: 
            return {}
        except Exception as e:
            return {
                'error': str(e)
            }, 500

