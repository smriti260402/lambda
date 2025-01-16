def lambda_handler(event, context):
    # Extract the numbers from the event (e.g., query parameters or JSON body)
    try:
        num1 = float(event['num1'])  # Assuming num1 is passed as part of the event
        num2 = float(event['num2'])  # Assuming num2 is passed as part of the event
    except (KeyError, ValueError):
        return {
            'statusCode': 400,
            'body': '{"message": "Invalid input. Please provide two numbers."}'
        }

    # Perform the addition
    result = num1 + num2

    # Return the result as the response
    return {
        'statusCode': 200,
        'body': f'{{"result": {result}}}'
    }
