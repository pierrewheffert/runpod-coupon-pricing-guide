#!/usr/bin/env python3
"""
RunPod GPU Pricing & Coupon Savings Calculator 2026.
Calculates monthly and annual GPU computing expenses across on-demand and reserved instances.
"""
import argparse

def calculate_costs(hours_per_month, gpu_rate, discount_percent):
    base_monthly = hours_per_month * gpu_rate
    discount_amount = base_monthly * (discount_percent / 100.0)
    effective_monthly = base_monthly - discount_amount
    annual_cost = effective_monthly * 12.0
    annual_savings = discount_amount * 12.0
    return {
        "base_monthly": base_monthly,
        "discount_amount": discount_amount,
        "effective_monthly": effective_monthly,
        "annual_cost": annual_cost,
        "annual_savings": annual_savings
    }

def main():
    parser = argparse.ArgumentParser(description="RunPod GPU Pricing & Savings Calculator")
    parser.add_argument("--hours", type=float, default=200.0, help="Monthly GPU compute hours (default: 200)")
    parser.add_argument("--rate", type=float, default=1.89, help="Hourly rate per GPU in USD (default: $1.89 for A100 80GB)")
    parser.add_argument("--discount", type=float, default=10.0, help="Promotional/referral discount percentage (default: 10%%)")
    args = parser.parse_args()

    res = calculate_costs(args.hours, args.rate, args.discount)
    print(f"Base Monthly Compute:    ${res['base_monthly']:.2f}")
    print(f"Discount Rate:           {args.discount:.1f}%")
    print(f"Monthly Savings:         ${res['discount_amount']:.2f}")
    print(f"Effective Monthly:       ${res['effective_monthly']:.2f}")
    print(f"Annual Total Compute:    ${res['annual_cost']:.2f}")
    print(f"Annual Total Savings:    ${res['annual_savings']:.2f}")

if __name__ == "__main__":
    main()
