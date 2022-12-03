# Project Repartis : 

:books: A peer-to-peer server based on Gnutella's approach :books:

## Usage :
```bash
python3 app.py
```

Files to be shared must be put in the 'shared' folder. Files must be present at app's startup, otherwise they won't be managed.

**_Note:_** Python 3.6 or above is required

## Little Desription : 

The application create the client peer and it needs at least another peer . <br>
The app either create an IPV4 socket or IPv6 socket . <br>
The files must be in `$(pwd)/shared` directory . <br>


## App architecture : 

Based on service/handler architecture :

> ### app.py : main app
> ### service : package for services
>   * AppData : data structures and methodes to interact with them
>   * Menu : the menu and the options traduction for MenuHandler
>   * Downloader : Connect to socket and download file
>   * Uploader : Upload file
>   * ServerThred : The isolated thread starting our server
> ### handler : package of handlers 
>   * HandlerInterface : An interace with serve method that is implemented in the other handlers 
>   * MenuHandler : handeling the commands given by the Menu service
>   * SelfHandler :
>   * NeighboursHandler :
> ### utils : package made for recyclable needed functions
>   * artist : util generating the ascii art of console
>   * UI_colors : shell colors to make the interacion between user and terminal easier
>   * proress_bar : an interactive progress bar for user
>   * SpinnerThread : a spinner for the user to show while he is waiting
>   * hasher : a function that hash a file for us
>   * Logger : class used to write into a logger with colors (useful for debug purposes)
>   * net_utils : getters and setters for networks prompt parameters (ipv4/ipv6/port....)



### Peer's supported commands:
[xxxB] = the parameter length in bytes
 
```shell
# Search a File
QUER[4B].Packet_Id[16B].IP_Peer[55B].Port_Peer[5B].TTL[2B].Research[20B]
# Server response will be
AQUE[4B].Packet_Id[16B].IP_Peer_j[55B].Port_Peer_j[5B].Filemd5[32B].Filename[100B]

# Search Neighbour
NEAR[4B].Packet_Id[16B].IP_Peer[55B].Port_Peer[5B].TTL[2B]
# Server response will be
ANEA[4B].Packet_Id[16B].IP_Peer_j[55B].Port_Peer_j[5B]

# Download a File
RETR[4B].Filemd5[32B]
# Server response will be
ARET[4B].\#chunk[3B].{Lenchunk_i[5B].data[LB]}(i=1..#chunk)
```

## Authors :rocket:

* **Oussema Jaouadi**
* **Taha Mediouni**

**Enjoy :sunglasses:**
