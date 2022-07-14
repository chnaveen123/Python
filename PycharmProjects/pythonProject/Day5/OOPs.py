class Player:

    def get_runs(self):
        print("runs Scores")

sachin = Player()
print(type(sachin))
sachin.get_runs()

print(isinstance(sachin,Player))
print(isinstance(sachin,object))
print(isinstance(sachin,str))

