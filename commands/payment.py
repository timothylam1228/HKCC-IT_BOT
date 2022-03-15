from telegram.error import BadRequest
from telegram import LabeledPrice
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def payment(update, context):
    try:

        chat_id = update.message.chat.id
        title = "HKCC OCAMP 費用"
        description = "HKCC OCAMP 費用"
        payload = '{}_{}'.format(chat_id, update.message.message_id)
        provider_token = "350862534:LIVE:YjYxZjNhMjNkNmY3"
        start_parameter = "TEMP"
        currency = "HKD"
        # prices = [LabeledPrice("HKCC OCAMP 費用", priceFromUser*100)]
        prices = [LabeledPrice("HKCC OCAMP 費用", 10000)]

        try:
            sent_invoice_message = context.bot.sendInvoice(chat_id=chat_id,
                                                           title=title,
                                                           description="HKCC OCAMP 費用",
                                                           payload=payload,
                                                           provider_token=provider_token,
                                                           start_parameter=payload,
                                                           currency=currency,
                                                           prices=prices)
        except BadRequest as e:
            error_string = str(e)
            logger.info('[%d] sendInvoice exception: %s',
                        chat_id, error_string, exc_info=True)
            update.message.reply_markdown(error_string=error_string)
            return
    except (ValueError):
        update.message.reply_text('咪玩野')

    # except IndexError:
    #     update.message.reply_text('請輸入範圍 1-25')


def ocampdetail(update, context):
    chat_id = update.message.chat.id
    f = open("ocamp.txt", "r")
    temp = f.read()
    # update.message.reply_text(text='INFO'+temp)
    context.bot.sendMessage(chat_id=chat_id, text=temp, parse_mode='HTML')


# @run_async
def precheckout_callback(update, context):
    query = update.pre_checkout_query
    context.bot.answerPreCheckoutQuery(update.pre_checkout_query.id, True)


def successful_payment_callback(bot, update):
    chat_id = update.message.chat_id
    logger.info('[%d] successful payment', chat_id)
    # https://core.telegram.org/bots/api#successfulpayment
    amount = update.message.successful_payment.total_amount

    bot.send_message(chat_id, text=(amount))
