import asyncio
import messagedumper
import pandas

async def main():
    channel = "https://t.me/Anti_Fake_News_Bot"

    messages = await messagedumper.dump_all_messages(channel, limit_msg=100, total_count_limit=2000)
    true_messages = []
    false_messages = []

    for message in messages:
        print(message)
        if str(message).find('ФЕЙК:') == -1: continue
        splited_message = str(message).split('ФЕЙК:')[1].split('ПРАВДА:')
        if len(splited_message) < 2: continue
        false_messages.append(splited_message[0])
        true_messages.append(splited_message[1])

    true_data = pandas.DataFrame()
    true_data['messages'] = true_messages
    true_data['labels'] = [0] * len(true_messages)

    false_data = pandas.DataFrame()
    false_data['messages'] = false_messages
    false_data['labels'] = [1] * len(false_messages)

    train_data = true_data.append(false_data, ignore_index=True)

    print(train_data)

    train_data.to_csv('false_and_true_data.csv', sep=';', index=False)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
