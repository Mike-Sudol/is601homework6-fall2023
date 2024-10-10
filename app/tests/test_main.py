'''Test Main''' 
from app.plugins.talk import TalkCommand

def test_calculate_and_print(capsys):
    ''' Test Main '''
    talk_command = TalkCommand()
    talk_command.execute(["Test"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello World!\n['Test']"
