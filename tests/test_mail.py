from send_email.mail import  set_values_to_send_emails, create_mock_send_email
import asyncio
import time
import pytest
@pytest.mark.asyncio
async def test_given_we_need_to_send_mails_when_we_send_it_with__concurrency_of_100_percent_then_the_time_total_is_less_or_equals_max_sleep_time():
    start_time = time.perf_counter()
    #given
    semaphore = asyncio.Semaphore(10)
    tasks = []
    mock_send_email = create_mock_send_email()
    csv_to_dict = [
    {"Email": "user0@gmail.com", "Subject": "Account Activation", "Body": "We have updated our terms and conditions."},
    {"Email": "user1@example.com", "Subject": "Important Update", "Body": "Here is your invoice for the recent purchase."},
    {"Email": "user2@hotmail.com", "Subject": "Your Invoice", "Body": "Thank you for signing up with us!"},
    {"Email": "user3@outlook.com", "Subject": "Welcome!", "Body": "Here is your invoice for the recent purchase."},
    {"Email": "user4@outlook.com", "Subject": "Your Invoice", "Body": "Here is your invoice for the recent purchase."},
    {"Email": "user5@hotmail.com", "Subject": "Account Activation", "Body": "Check out our latest news and updates!"},
    {"Email": "user6@gmail.com", "Subject": "Important Update", "Body": "Here is your invoice for the recent purchase."},
    {"Email": "user7@outlook.com", "Subject": "Your Invoice", "Body": "Here is your invoice for the recent purchase."},
    {"Email": "user8@hotmail.com", "Subject": "Important Update", "Body": "We have updated our terms and conditions."}
    ]
    try:
        #when
        for row in csv_to_dict:
            tasks.append(asyncio.create_task(set_values_to_send_emails(semaphore, mock_send_email, row['Email'])))
    except:
        raise("error")
    await asyncio.gather(*tasks)
    end_time = time.perf_counter()
    time_final = end_time-start_time
    #then
    assert time_final <= 5



@pytest.mark.asyncio
async def test_given_we_need_to_send_mails_when_we_send_it_with__concurrency_of_10_percent_then_the_time_total_is_less_or_equal_of_the_equivalent_max_time_and_highr_than_the_equivalent_less_time():
    start_time = time.perf_counter()
    #given
    semaphore = asyncio.Semaphore(1)
    tasks = []
    mock_send_email = create_mock_send_email()
    csv_to_dict = [
    {"Email": "user0@gmail.com", "Subject": "Account Activation", "Body": "We have updated our terms and conditions."},
    {"Email": "user1@example.com", "Subject": "Important Update", "Body": "Here is your invoice for the recent purchase."},
    {"Email": "user2@hotmail.com", "Subject": "Your Invoice", "Body": "Thank you for signing up with us!"},
    {"Email": "user3@outlook.com", "Subject": "Welcome!", "Body": "Here is your invoice for the recent purchase."},
    {"Email": "user4@outlook.com", "Subject": "Your Invoice", "Body": "Here is your invoice for the recent purchase."},
    {"Email": "user5@hotmail.com", "Subject": "Account Activation", "Body": "Check out our latest news and updates!"},
    {"Email": "user6@gmail.com", "Subject": "Important Update", "Body": "Here is your invoice for the recent purchase."},
    {"Email": "user7@outlook.com", "Subject": "Your Invoice", "Body": "Here is your invoice for the recent purchase."},
    {"Email": "user8@hotmail.com", "Subject": "Important Update", "Body": "We have updated our terms and conditions."}
    ]
    try:
        #when
        for row in csv_to_dict:
            tasks.append(asyncio.create_task(set_values_to_send_emails(semaphore, mock_send_email, row['Email'])))
    except:
        raise("error")
    await asyncio.gather(*tasks)
    end_time = time.perf_counter()
    time_final = end_time-start_time
    #then
    assert time_final <= 50 and time_final>= 9


@pytest.mark.asyncio
async def test_given_we_have_a_fail_rate_when_we_send_the_mails_we_have_the_equivalent_fail_emails_sent():
    global err_count
    err_count = 0
    semaphore = asyncio.Semaphore(1)
    tasks = []
    mock_send_email = create_mock_send_email(fail_rate=0.2)
    csv_to_dict = [
    {"Email": "user0@gmail.com", "Subject": "Account Activation", "Body": "We have updated our terms and conditions."},
    {"Email": "user1@example.com", "Subject": "Important Update", "Body": "Here is your invoice for the recent purchase."},
    {"Email": "user2@hotmail.com", "Subject": "Your Invoice", "Body": "Thank you for signing up with us!"},
    {"Email": "user3@outlook.com", "Subject": "Welcome!", "Body": "Here is your invoice for the recent purchase."},
    {"Email": "user4@outlook.com", "Subject": "Your Invoice", "Body": "Here is your invoice for the recent purchase."},
    {"Email": "user5@hotmail.com", "Subject": "Account Activation", "Body": "Check out our latest news and updates!"},
    {"Email": "user6@gmail.com", "Subject": "Important Update", "Body": "Here is your invoice for the recent purchase."},
    {"Email": "user7@outlook.com", "Subject": "Your Invoice", "Body": "Here is your invoice for the recent purchase."},
    {"Email": "user8@hotmail.com", "Subject": "Important Update", "Body": "We have updated our terms and conditions."},
    {"Email": "user9@hotmail.com", "Subject": "Important Update", "Body": "We have updated our terms and conditions."}
    ]
    try:
        for row in csv_to_dict:
            tasks.append(asyncio.create_task(set_values_to_send_emails(semaphore, mock_send_email, row['Email'])))
    except:
        raise("error")
    await asyncio.gather(*tasks)
    assert err_count == 2

