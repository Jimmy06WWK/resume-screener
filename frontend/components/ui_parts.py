import streamlit as st
import time

def render_metric_cards(results):
    """Render premium metric cards"""
    if not results:
        return
    
    col1, col2, col3, col4 = st.columns(4)
    
    metrics = [
        (len(results), "Total Candidates"),
        (f"{sum(r['score'] for r in results) / len(results):.1f}%", "Average Score"),
        (f"{max(r['score'] for r in results)}%", "Top Score"),
        (f"{len([r for r in results if r['score'] >= 70]) / len(results) * 100:.0f}%", "Passing Rate")
    ]
    
    for col, (value, label) in zip([col1, col2, col3, col4], metrics):
        with col:
            st.markdown(f"""
                <div class="metric-card-premium">
                    <div class="metric-value">{value}</div>
                    <div class="metric-label">{label}</div>
                </div>
            """, unsafe_allow_html=True)

def render_loading_animation():
    """Show premium loading animation"""
    st.markdown("""
        <div class="premium-loader">
            <div class="loader-ring">
                <div></div><div></div><div></div>
            </div>
            <p style="margin-top: 1.5rem; color: #5b8caf; font-weight: 500;">AI is analyzing resumes...</p>
            <p style="color: #7a9bb0; font-size: 0.8rem;">Using advanced AI algorithms</p>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(1)

def render_candidate_card(data, index=0):
    """Render premium candidate card"""
    
    # Determine badge
    if data['score'] >= 85:
        badge_class = "badge-excellent"
        badge_text = "Exceptional"
    elif data['score'] >= 70:
        badge_class = "badge-good"
        badge_text = "Strong Match"
    elif data['score'] >= 55:
        badge_class = "badge-fair"
        badge_text = "Good Match"
    else:
        badge_class = "badge-review"
        badge_text = "Needs Review"
    
    # Calculate circle dashoffset
    radius = 35
    circumference = 2 * 3.14159 * radius
    dashoffset = circumference * (1 - data['score'] / 100)
    
    st.markdown(f"""
        <div class="candidate-card-premium" style="animation-delay: {index * 0.05}s;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                <div style="display: flex; align-items: center; gap: 1rem;">
                    <div class="rank-badge-premium">#{index + 1}</div>
                    <div>
                        <h3 class="candidate-name-premium">{data['candidate_name']}</h3>
                        <div style="margin-top: 0.5rem;">
                            <span class="{badge_class}">{badge_text}</span>
                        </div>
                    </div>
                </div>
                <div class="score-container">
                    <svg width="80" height="80" viewBox="0 0 80 80">
                        <circle class="score-ring-bg" cx="40" cy="40" r="35" stroke-width="6" fill="none"/>
                        <circle class="score-ring-fill" cx="40" cy="40" r="35" stroke-width="6" fill="none"
                                stroke-dasharray="{circumference}" stroke-dashoffset="{dashoffset}"
                                transform="rotate(-90 40 40)"/>
                        <defs>
                            <linearGradient id="scoreGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" stop-color="#7bc0d4"/>
                                <stop offset="100%" stop-color="#5b8caf"/>
                            </linearGradient>
                        </defs>
                        <text x="40" y="46" text-anchor="middle" class="score-text">{data['score']}%</text>
                    </svg>
                </div>
            </div>
            <p style="color: #7a9bb0; line-height: 1.6; margin-top: 0.5rem;">{data.get('reason', '')[:180]}...</p>
        </div>
    """, unsafe_allow_html=True)
    
    with st.expander("View Detailed Analysis"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Matched Skills**")
            for s in data.get('matched_skills', [])[:6]:
                st.caption(f"• {s}")
        with col2:
            st.markdown("**Missing Skills**")
            for s in data.get('missing_skills', [])[:6]:
                st.caption(f"• {s}")
        
        st.divider()
        col_a, col_b = st.columns(2)
        with col_a:
            st.info(f"**Strengths**\n" + "\n".join([f"• {s}" for s in data.get('strengths', [])[:3]]))
        with col_b:
            st.warning(f"**Concerns**\n" + "\n".join([f"• {c}" for c in data.get('concerns', [])[:3]]))
