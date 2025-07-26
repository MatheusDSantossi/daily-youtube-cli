from youtube_utils import open_playlist, open_personal_playlist, extract_id, make_my_personal_playlist_url, inform_videos_urls

def main():
      def menu():
            print("""
                  -----------------------------------
                  Welcome to your YouTube video automation. You can send the videos urls you want and we'll  open YouTube for you and add them to your playlist. 
                  -----------------------------------
                  Below you just need to pass a list of the urls videos or exactly videos names you want to wactch, Example:
                  
                  https://youtu.be/abc123, dQw4w9WgXcQ, https://www.youtube.com/watch?v=XYZ789
                  """)

      def menu_options():
            print("""
                  Select one of the options:
                  1- Play your personal video playlist
                  2- Inform videos urls
                  3- Create a personal video playlist
                  
                  4- Exit
                  """)


      menu()
      menu_options()

      option = int(input("Type your option: "))

      while True:

            if option == 1:
                  open_personal_playlist()
                  break
                  
            elif option == 2:
                  inform_videos_urls()
                  break
                  
            elif option == 3:
                  break
            
            else:
                  print("Type a valid option!")
                  menu_options()
                  option = int(input("Type your option: "))


