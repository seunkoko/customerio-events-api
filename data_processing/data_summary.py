import json
import time


def file_summary(filename):
    """Summarizes Customerio event data file
    Args
        expected_args(string): filename
    Returns
        None
    """
    no_of_lines = 1 # keeps track of file lines
    processed_data = {} # keeps track of summarized data
    processed_event_ids = set() # keeps track of event ids

    start = time.time() # start of function time
    
    with open(filename) as file: 
        # read file by line
        while (line := file.readline().rstrip()):
            _data = json.loads(line) # json parse each line

            # check if user_id is in data
            if "user_id" in _data:
                # handle when data type is attributes
                if _data['type'] == 'attributes':
                    # check if user_id has been processed/summarized previously
                    if _data['user_id'] in processed_data:
                        # check if attributes type has been processed/summarized previously for user_id
                        if 'attributes' in processed_data[_data['user_id']]:
                            # check if summarized attribute's timestamp is less than new attribute timestamp
                            if processed_data[_data['user_id']]['last_updated'] <= _data['timestamp']:
                                # update summarized attribute with new attributes data
                                processed_data[_data['user_id']] = update_customer_attribute(processed_data[_data['user_id']], _data)
                        else:
                            # create attribute summary for user_id
                            processed_data[_data['user_id']] = customer_summary_attribute(processed_data[_data['user_id']], _data)
                    else:
                        # summarize user_id's data and attributes
                        processed_data[_data['user_id']] = customer_summary(_data)
                        processed_data[_data['user_id']] = customer_summary_attribute(processed_data[_data['user_id']], _data)

                # handle when data type is event
                if _data['type'] == 'event':
                    # check if user_id has been processed/summarized previously
                    if _data['user_id'] in processed_data:
                        # check if event type has been processed/summarized previously for user_id
                        if 'events' in processed_data[_data['user_id']]:
                            # check if event id is unique
                            if _data['id'] not in processed_event_ids:
                                # update summarized event with new event data
                                processed_data[_data['user_id']] = update_customer_event(processed_data[_data['user_id']], _data)
                                # keep track of processed event ids
                                processed_event_ids.add(_data['id'])
                        else:
                            # create event summary for user_id
                            processed_data[_data['user_id']] = customer_summary_event(processed_data[_data['user_id']], _data)
                    else:
                        # summarize user_id's data and event
                        processed_data[_data['user_id']] = customer_summary(_data)
                        processed_data[_data['user_id']] = customer_summary_event(processed_data[_data['user_id']], _data)

            no_of_lines+=1
        
    end = time.time() # end of function time

    # write processed data in file
    f = open("data/summary.data", "w")
    f.write(json.dumps(processed_data))
    f.close()

    print("\n\n",len(processed_data), 'users') # print total users
    print(end - start, 'Function time') # print function time
    print(no_of_lines, 'no of lines', "\n\n") # print no of file lines processed


def customer_summary(data):
    return {
        "id": data['user_id']
    }

def customer_summary_attribute(summarized_data, new_data):
    return {
        **summarized_data,
        "attributes": new_data["data"],
        "last_updated": new_data["timestamp"] if "timestamp" in new_data else None
    }

def customer_summary_event(summarized_data, new_data):
    return {
        **summarized_data,
        "events": {
            new_data['name']: 1 
        }
    }

def update_customer_attribute(old_data, new_data):
    return {
        **old_data, 
        "attributes": {
            **old_data['attributes'],
            **new_data["data"]
        },
        "last_updated": new_data["timestamp"] if "timestamp" in new_data else None
    }

def update_customer_event(old_data, new_data):
    return {
        **old_data, 
        "events": {
            **old_data['events'],
            new_data['name']: old_data['events'][new_data['name']] + 1 if new_data['name'] in old_data['events'] else 1
        }
    }
