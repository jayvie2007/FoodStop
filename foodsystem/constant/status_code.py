from rest_framework import status

################STATUS_CODE##################
ok = status.HTTP_200_OK
created = status.HTTP_201_CREATED
not_found = status.HTTP_404_NOT_FOUND
error = status.HTTP_400_BAD_REQUEST
no_data = status.HTTP_204_NO_CONTENT

no_info = ("data not found")