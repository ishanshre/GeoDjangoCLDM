# Retrive All Delivery Locations

## Descrption:
    - This API endpoint, avaliable at 'localhost:8000/api/v1/delivery-locations', is designed to retrieve a list of all delivery locations stored in the system. It provides access to comprehensive information about each delivery location, including its name, geographic coordinates, and additional details.

### Usuage:
    - HTTP Method: GET
    - URL: `http://localhost:8000/api/v1/delivery-locations`
    - URL: `http://localhost:8000/api/v1/delivery-locations/{id}`

### Query Parameters (Optional):
    - limit (default: 10) - Limit specifies the maximum number of items (resources) that should be returned.
    - offset (default: 0) - Offset specifies the starting point from which the API should begin returning items.
    - is_primary (no default) - Filter query paramater that filters customer's default delivery locations

### Example Request with limit and offset:
    ```
    curl --location 'http://localhost:8000/api/v1/delivery-locations?limit=10&offset=0'
    ```

### Example Response:
    ```
    {
        "count": 12,
        "next": "http://localhost:8000/api/v1/delivery-locations/?limit=10&offset=10",
        "previous": null,
        "results": {
            "type": "FeatureCollection",
            "features": [
                {
                    "id": 1,
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            30.031064,
                            -1.972112
                        ]
                    },
                    "properties": {
                        "location_name": "Dont know",
                        "is_primary": false,
                        "customer_name": "Ishan"
                    }
                },
                {
                    "id": 6,
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            85.44342,
                            27.763229
                        ]
                    },
                    "properties": {
                        "location_name": "Nepa~laya",
                        "is_primary": true,
                        "customer_name": "Ishan"
                    }
                },
                ... // hidden
                {
                    "id": 7,
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            84.435425,
                            27.945886
                        ]
                    },
                    "properties": {
                        "location_name": "Gausala",
                        "is_primary": true,
                        "customer_name": "admin"
                    }
                }
            ]
        }
    }    
    ```

### Example Request with limit and offset:
    ```
    curl --location 'http://localhost:8000/api/v1/delivery-locations?limit=10&offset=0&is_primary=true'
    ```

### Example Response
    ```
    {
        "count": 2,
        "next": null,
        "previous": null,
        "results": {
            "type": "FeatureCollection",
            "features": [
                {
                    "id": 6,
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            85.44342,
                            27.763229
                        ]
                    },
                    "properties": {
                        "location_name": "Nepa~laya",
                        "is_primary": true,
                        "customer_name": "Ishan"
                    }
                },
                {
                    "id": 7,
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            84.435425,
                            27.945886
                        ]
                    },
                    "properties": {
                        "location_name": "Gausala",
                        "is_primary": true,
                        "customer_name": "admin"
                    }
                }
            ]
        }
    }
    ```

### Example Request using ID:
    ```
    curl --location 'http://localhost:8000/api/v1/delivery-locations/2'
    ```

### Example Response:
    ```
    {
        "id": 2,
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [
                85.312808,
                27.711813
            ]
        },
        "properties": {
            "location_name": "Ratna park",
            "is_primary": false,
            "customer_name": "Ishan"
        }
    }
    ```
