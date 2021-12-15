from website.models import Product, UserDetails, Auction, Bid
from django.utils import timezone
from datetime import datetime, timedelta


def increase_bid(user, auction, bidAmount):
    """
    Removes €1.0 from user.
    Creates a Bid record
    Increases the auction's number of bids

    Parameters
    ----------
    auction : class 'website.models.Auction
    """
    
    userDetails = UserDetails.objects.get(id=user.id)
    userDetails.balance = float(userDetails.balance) - 0.5
    userDetails.save()
    
    bid = Bid()
    bid.user_id = user
    bid.auction_id = auction
    bid.bid_time = timezone.now()
    bid.bidAmount = bidAmount
    bid.save()
    auction.number_of_bids += 1
    auction.time_ending = timezone.now() + timedelta(minutes=3) #hereeeee where we are fixing the time for the auction process
    auction.currentBidAmount += bidAmount
    auction.save()

def increase_bid_shareable_product(user, auction, bidAmount, bidQuantity, score):
    """
    Removes €1.0 from user.
    Creates a Bid record
    Increases the auction's number of bids

    Parameters
    ----------
    auction : class 'website.models.Auction
    """
    
    userDetails = UserDetails.objects.get(id=user.id)
    userDetails.balance = float(userDetails.balance) - 1
    userDetails.save()
    
    bid = Bid()
    bid.user_id = user
    bid.auction_id = auction
    bid.bid_time = timezone.now()
    bid.bidAmount = bidAmount  #in the shareable case, this is the base price proposed
    bid.score = score
    bid.qte = bidQuantity
    bid.base_price = bidAmount
    bid.save()
    auction.number_of_bids += 1
    auction.time_ending = timezone.now() + timedelta(minutes=3) #hereeeee where we are fixing the time for the auction process
    auction.save()    


def remaining_time(auction):
    """
    Calculates the auction's remaining time
    in minutes and seconds and converts them 
    into a string.

    Parameters
    ----------
    auction : class 'website.models.Auction

    Returns
    -------

    time_left : str
        string representation of remaining time in
        minutes and seconds.
    expired : int
        if the value is less than zero then the auction ended.

    """
    time_left = auction.time_ending - timezone.now()
    days, seconds = time_left.days, time_left.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    time_left = str(minutes) + "m " + str(seconds) + "s"
    expired = days

    return time_left, expired
