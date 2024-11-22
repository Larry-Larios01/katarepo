from send_email.mail import  set_values_to_send_emails, create_mock_send_email
import asyncio
import time
import pytest
@pytest.mark.asyncio
async def test_given_we_need_to_send_mails_when_we_send_it_with__concurrency_of_100_percent_then_the_time_total_is_less_or_equals_max_sleep_time():
    start_time = time.perf_counter()
    #given
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
    results = await set_values_to_send_emails(csv_to_dict,0.2,10)
    end_time = time.perf_counter()
    time_final = end_time-start_time
    results.time_total = time_final
    #then
    assert time_final <= 5



@pytest.mark.asyncio
async def test_given_we_need_to_send_mails_when_we_send_it_with__concurrency_of_10_percent_then_the_time_total_is_less_or_equal_of_the_equivalent_max_time_and_highr_than_the_equivalent_less_time():
    start_time = time.perf_counter()
    #given
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
    #when
    results = await set_values_to_send_emails(csv_to_dict,0.2,1)
    end_time = time.perf_counter()
    time_final = end_time-start_time
    results.time_total = time_final
    #then
    assert time_final <= 50 and time_final>= 9


@pytest.mark.asyncio
async def test_given_we_have_a_fail_rate_when_we_send_the_mails_we_have_the_equivalent_fail_emails_sent():
    
    global ok_count, err_count, ok_time, err_time
    ok_count, err_count, ok_time, err_time = 0, 0, 0, 0
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
    
    
    results = await set_values_to_send_emails(csv_to_dict,0.2,10)

    
    assert results.err_count == 2


@pytest.mark.asyncio
async def test_given_we_have_a_fails_and_ok_mails_when_we_sum_then_we_have_the_len_of_list():
    
    #given
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
    results = await set_values_to_send_emails(csv_to_dict,0.2,10)
    assert (results.err_count+results.ok_count) == len(csv_to_dict)
