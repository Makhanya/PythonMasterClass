"""
Http Introduction
    Describe what happens when you type a URL in the URL bar
    Describe the request/response cycle
    Explain what a request or response header is, and give examples
    Explain the different categories of response codes
    Compare Get and Post requests

The internet
    What happends when...
        1.DNS lookup
            Like a Phonebook for the internet
            google.com -> DNS server -> 172.217.9.142     

        2.Computer makes a REQUEST to a server
            Requests and Request
                Client(Computer) -> Get -> Server
                Client <- 200 OK <- Server

        3.Server processes that REQUEST
            HTTP Headers
                Sent with both requests and responses
                Provide additional information about the request and response
            HTTP Examples
                Request Headers
                    *Accept - Acceptable content-types for response(eg. HTML, JSON, XML)
                    *Cache-Controll - Specify caching behavior
                    *User-Agent - Information about the software used to make the request
                Response Headers
                    *Access-Control-Allow-Origin - Specify domains that can make requests
                    *Allowed - HTTP verbs that are allowed in requests
       
        4.Server issues a RESPONSE
             Response status Codes
                2xx - success
                3xx - redireect
                4xx - Client Error (Your failt)
                5xx - Server Error(not your fault)
        request/Response cycle
    
    HTTP Verbs
        GET
            Useful for retrieving Data
            Data passed in query string
            Should have no "side-effects"
            Can be cached
            Can be bookmarked
        POST
            Useful for writing data
            Data passed in request body
            Can have "side-effects"
            Not cached
            Can't be bookmarked

        APIs
            API - Application Programming Interface
            Allows you to get data from another application without needing
                to understand how the application works
            Can often send back in different formats
            Examples of companies with APIs:Github,Spotify, Google

            
    """