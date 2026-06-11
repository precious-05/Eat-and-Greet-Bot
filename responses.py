# responses.py - Eat and Greet Restaurant Bot

import re

def get_response(user_message):
    """Eat and Greet restaurant ka reply generator"""
    
    msg = user_message.lower().strip()
    
    # Greetings
    if any(word in msg for word in ['hi', 'hello', 'hey', 'salam', 'assalam', 'good morning', 'good evening']):
        return "Welcome to Eat and Greet! I can help you with: Menu and Prices, Table Booking, Delivery Info, Opening Hours, Order Tracking. What would you like to know?"
    
    # Menu
    elif any(word in msg for word in ['menu', 'food', 'dish', 'khaana', 'kya hai', 'items', 'what do you have']):
        return "Eat and Greet Menu: Desi Mains: Karahi, Nihari, Haleem (PKR 800-2500) | Grills: Seekh Kebab, Chicken Tikka (PKR 600-1800) | Burgers: Special Burger (PKR 400-900) | Rice: Biryani, Pulao (PKR 350-1200) | Deals: Family Deal PKR 1200-4500 | Desserts: Gulab Jamun (PKR 150-500). Which would you like to order?"
    
    # Pricing
    elif any(word in msg for word in ['price', 'cost', 'rate', 'kitna', 'pkr', 'rupee', 'how much']):
        return "Price Range: Desi Mains PKR 800-2500 | Grills and BBQ PKR 600-1800 | Burgers and Wraps PKR 400-900 | Rice Dishes PKR 350-1200 | Deals PKR 1200-4500 | Beverages and Desserts PKR 150-500. Want our special combo deals? Just ask!"
    
    # Delivery
    elif any(word in msg for word in ['delivery', 'deliver', 'ghar', 'home', 'area', 'multan', 'lahore', 'karachi', 'islamabad']):
        if 'multan' in msg or 'lahore' in msg or 'karachi' in msg:
            return "Delivery to your city available! Time: 60-90 minutes. Delivery charges: PKR 100. Free delivery on orders above PKR 1500. Want to place an order? DM your address and items!"
        else:
            return "Delivery Information: Major cities 30-45 minutes | Other areas 60-90 minutes | Delivery fee PKR 100 | Free delivery on orders PKR 1500+. Ready to order? Tell me your city!"
    
    # Reservation and Booking
    elif any(word in msg for word in ['book', 'reserve', 'table', 'seat', 'dine', 'reservation', 'booking']):
        return "Table Booking at Eat and Greet: Tables available for 2-20 people. Book 2 hours in advance. Call or DM to confirm. Deposit required for groups above 10. DM me: Name, Date, Time, Number of guests! Call us: 0321-1234567"
    
    # Opening Hours
    elif any(word in msg for word in ['open', 'close', 'time', 'hours', 'kab', 'timing', 'operating']):
        return "Eat and Greet Timings: Monday-Thursday 12:00 PM to 12:00 AM | Friday 1:00 PM to 1:00 AM | Saturday-Sunday 11:00 AM to 1:00 AM. We are open late! Visit us anytime!"
    
    # Payment
    elif any(word in msg for word in ['pay', 'payment', 'jazzcash', 'easypaisa', 'cod', 'card', 'cash', 'bank']):
        return "Payment Options: JazzCash, EasyPaisa, Bank Transfer, Credit and Debit Card, Cash on Delivery. COD available in all major cities. Pay the way you like!"
    
    # Deals and Offers
    elif any(word in msg for word in ['deal', 'discount', 'offer', 'combo', 'special', 'promo']):
        return "Special Offers: Family Deal for 4-5 persons PKR 2500 | Couple Deal PKR 1200 | Student Special PKR 800. New deals every Monday! Follow eatandgreetofficial on Instagram. Ask me about today's special!"
    
    # Order Status
    elif any(word in msg for word in ['order', 'track', 'status', 'where', 'kahan', 'delivered', 'dispatch']):
        return "Order Tracking: Please share your Order ID or Registered Phone Number. We will send tracking updates via WhatsApp after dispatch. DM me your details and I will check!"
    
    # Cancellation
    elif any(word in msg for word in ['cancel', 'cancellation', 'return']):
        return "Cancellation Policy: Online orders can be cancelled within 5 minutes of placing. Call restaurant directly for urgent changes. Need to cancel? Act fast!"
    
    # Fallback - if nothing matches
    else:
        return "Thank you for reaching out to Eat and Greet! Our team will get back to you within 15 minutes. Follow us: @eatandgreetofficial | Website: eatandgreet.com. For quick response, try: 'menu' for our dishes, 'delivery' for delivery info, 'timings' for opening hours. How can I help you today?"