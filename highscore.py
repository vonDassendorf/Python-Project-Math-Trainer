class HighscoreList():
    def __init__(self, exercise, username, points):
        ##Creating and loading the Highscore list##
        self.highscore_list = {'add': {},'sub': {},'div': {},'mul': {}}
        self.highscore_list_file = open("highscore.txt", "w")
        #self.highscore_add(exercise, username, points)

        ##Adding results to highscore##
    def highscore_add(self, exercise, username, points):
        if exercise == "+":
            if len(self.highscore_list['add'].keys()) < 10 and result > min(self.highscore_list,
                                            key=self.highscore_list.get):
                self.highscore_list['add'][username] = points
            elif result > min(self.highscore_list, key=self.highscore_list.get):
                self.highscore_list.pop([min(self.highscore_list,
                                            key=self.highscore_list.get)], None)
                self.highscore_list['add'][username] = points
