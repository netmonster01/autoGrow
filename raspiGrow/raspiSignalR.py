from requests import Session
from requests.auth import HTTPBasicAuth
from signalr import Connection


def main():
    with Session() as session:
        session.auth = HTTPBasicAuth("known", "user")
        #connection = Connection("http://localhost:16338/signalr", session)
        connection = Connection("http://netmonsterraspisignalr.azurewebsites.net",session)
        #connection = Connection("http://localhost:5000/signalr", session)
        chat = connection.register_hub('raspiGrowHub')

        def print_received_message(name, message):
            print('received: ', message)

        def print_error(error):
            print('error: ', error)

        chat.client.on('addNewMessageToPage', print_received_message)
        #chat.client.on('topicChanged', print_topic)

        connection.error += print_error

        with connection:
            chat.server.invoke('send', 'Kris','Python is here!')
            #chat.server.invoke('setTopic', 'Welcome python!')
            #chat.server.invoke('requestError')
            #chat.server.invoke('send', 'Bye-bye!')

            connection.wait(1)


if __name__ == "__main__":
    main()