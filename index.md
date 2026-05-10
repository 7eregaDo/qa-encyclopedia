---
layout: home
---

<div style="padding: 40px 0; text-align: center;">
  <h1 style="font-size: 3.5rem; letter-spacing: -2px; margin-bottom: 10px;">
    QA <span style="color: #8b5cf6;">Encyclopedia</span>
  </h1>
  <p style="color: #94a3b8; font-size: 1.2rem; max-width: 700px; margin: 0 auto;">
    A high-fidelity knowledge base for modern Quality Engineering.
  </p>
</div>

<div class="category-grid">
  {% for cat in site.data.categories %}
  <a class="category-card" href="{{ site.baseurl }}/{{ cat.slug }}/">
    <div style="font-size: 1.5rem; color: #06b6d4;">{{ cat.icon }}</div>
    <h3>{{ cat.name }}</h3>
    <p>{{ cat.description }}</p>
    <div style="margin-top: 15px; color: #8b5cf6; font-size: 0.75rem; font-weight: bold; letter-spacing: 1px; text-transform: uppercase;">
      {{ cat.levels | join: " • " }}
    </div>
  </a>
  {% endfor %}
</div>

<div style="margin-top: 60px;">
  <h2 style="border-left: 4px solid #06b6d4; padding-left: 15px; margin-bottom: 20px;">📊 Domain Coverage</h2>
  
  <table class="stats-table">
    <thead>
      <tr>
        <th>Category</th>
        <th>Entry</th>
        <th>Mid</th>
        <th>Senior</th>
        <th>Lead</th>
        <th>Total</th>
      </tr>
    </thead>
    <tbody>
      {% for cat in site.data.categories %}
        {% assign cat_qs = site.questions | where: "category", cat.slug %}
        <tr>
          <td><span style="color: #94a3b8; margin-right: 8px;">{{ cat.icon }}</span> <strong>{{ cat.name }}</strong></td>
          {% assign levels = "entry,mid,senior,lead" | split: "," %}
          {% for lvl in levels %}
            <td style="text-align: center;">
              {% assign count = cat_qs | where: "level", lvl | size %}
              {% if count > 0 %}
                <a href="{{ site.baseurl }}/{{ cat.slug }}/{{ lvl }}/">{{ count }}</a>
              {% else %}
                <span style="opacity: 0.1;">—</span>
              {% endif %}
            </td>
          {% endfor %}
          <td style="text-align: center; font-weight: bold; color: #06b6d4;">{{ cat_qs | size }}</td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
</div>