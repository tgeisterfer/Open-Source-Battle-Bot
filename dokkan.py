import commands
import config

config.identifier = commands.signup()
config.access_token,config.secret = commands.signin(config.identifier)
#commands.db_download()
commands.tutorial()
commands.complete_stage('1001','0')
commands.accept_missions()
commands.accept_gifts()
#commands.change_team()
#commands.get_kagi_id('310001')
commands.complete_unfinished_quest_stages()

