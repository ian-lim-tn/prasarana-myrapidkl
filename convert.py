import json
from google.transit import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToJson

def convert_proto_to_json(input_file, output_file):
    # Initialize the FeedMessage object
    feed = gtfs_realtime_pb2.FeedMessage()
    
    try:
        # Read the binary .proto file
        with open(input_file, 'rb') as f:
            feed.ParseFromString(f.read())
        
        # Convert the Protobuf message to a JSON string
        json_data = MessageToJson(feed)
        
        # Save to file
        with open(output_file, 'w') as f:
            f.write(json_data)
            
        print(f"Successfully converted {input_file} to {output_file}")
        
    except Exception as e:
        print(f"Error: {e}. Ensure the file is a valid binary Protobuf message.")

# Run the conversion
convert_proto_to_json('vehicle-position-prasarana.proto', 'vehicle_positions.json')