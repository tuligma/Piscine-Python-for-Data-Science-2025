#!/bin/bash


if [ $# -eq 1 ] && [ "$1" == "data scientist" ]; then
  curl -s -H "User-Agent: api-test-agent" \
    "https://api.hh.ru/vacancies?text=data%20scientist&per_page=20&page=0" \
  | jq '{
      page,
      found,
      clusters,
      arguments,
      per_page,
      pages,
      items: [.items[]]
    }' > hh.json
  echo "Data saved to hh.json"
else
  echo "Usage: $0 'data scientist'"
  exit 1
fi



# if [ $# -eq 1 ] && [ "$1" == "data scientist" ]; then
#   curl -s -H "User-Agent: api-test-agent" \
#     "https://api.hh.ru/vacancies?text=data%20scientist&per_page=20&page=0" \
#   | jq '{
#       page,
#       found,
#       clusters,
#       arguments,
#       per_page,
#       pages,
#       items: [
#         .items[] | {
#           apply_alternate_url: .apply_alternate_url,
#           address: {
#             id: .address.id,
#             lat: .address.lat,
#             metro: {
#               station_id: .address.metro.station_id,
#               line_name: .address.metro.line_name,
#               lng: .address.metro.lng,
#               line_id: .address.metro.line_id,
#               station_name: .address.metro.station_name,
#               lat: .address.metro.lat
#             },
#             street: .address.street,
#             lng: .address.lng,
#             metro_stations: (
#               .address.metro_stations // [] | map({
#                 line_name : .line_name,
#                 station_id: .station_id,
#                 lng: .lng,
#                 line_id: .line_id,
#                 lat: .lat,
#                 station_name: .station_name
#               })
#             )
#           },
#           building: .building,
#           city: .city,
#           description: .description,
#           raw: .raw
#         }
#       ]
#     }' > hh.json
#   echo "Data saved to hh.json"
# else
#   echo "Usage: $0 'data scientist'"
#   exit 1
# fi

# curl -s -H "User-Agent: api-test-agent" \
#      "https://api.hh.ru/vacancies?text=data%20scientist&per_page=20&page=0" \
# | jq '.' > hh.json
