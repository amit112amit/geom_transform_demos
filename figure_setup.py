import matplotlib.pyplot as plt

from bokeh.models import ColumnDataSource, Label, FreehandDrawTool, PolyDrawTool
from bokeh.plotting import figure
from numpy import allclose, array, c_, eye
from string import ascii_uppercase


def showplot(H, X=None, axisrange=(-2, 2), textoffset=0.1):
    """
    Create a figure with plot of points in `X` before and after the
    transformation `H`.
    """
    # The coordinates before transformation
    if X is None:
        X = array([[1.5, 0.75, 0.5],
                  [1, 1.5, 0.5],
                  [1, 1, 1]])
        
    # The coordinates after transformation
    Xp = H @ X
    
    # If the last row of H is not [0, 0, 1] we need to rescale
    if not allclose(H[2], [0, 0, 1]):
        for i in range(Xp.shape[1]):
            Xp[:, i] /= Xp[-1, i]

    # To plot closed figures we will append the first column
    X_closed = c_[X, X[:,0]]
    Xp_closed = c_[Xp, Xp[:,0]]
    
    # Set up the figure
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.set_xlim(*axisrange)
    ax.set_ylim(*axisrange)
    
    # Mark the origin
    ax.plot(0.0, 0.0, marker='+', markersize=10)

    # The shape before transformation
    ax.plot(X_closed[0, :], X_closed[1, :], marker='o', markersize=5, color='darkgrey', label='Before')
    for col, label in zip(X.T, ascii_uppercase):
        ax.text(x=col[0] + textoffset, y=col[1] + textoffset, s=label, color='darkgrey', fontsize=12)

    # The shape after transformation
    ax.plot(Xp_closed[0, :], Xp_closed[1, :], marker='o', markersize=5, color='red', label='After')
    for col, label in zip(Xp.T, ascii_uppercase):
        ax.text(x=col[0] + textoffset, y=col[1] + textoffset, s=f"{label}'", color='red', fontsize=12)
        
    # Display legends
    ax.legend()
    
    # Close the pyplot figure
    plt.close()
    
    return fig


def makeplot(H, X=None, axisrange=(-2, 2)):
    """
    Create a figure with plot of points in `X` before and after the
    transformation `H`.
    """
    # The coordinates before transformation
    if X is None:
        X = array([[1.5, 0.75, 0.5],
                  [1, 1.5, 0.5],
                  [1, 1, 1]])
        
    # The coordinates after transformation
    Xp = H @ X

    # If the last row of H is not [0, 0, 1] we need to rescale
    if not allclose(H[2], [0, 0, 1]):
        for i in range(Xp.shape[1]):
            Xp[:, i] /= Xp[-1, i]
            
    # To plot closed figures we will append the first column
    X_closed = c_[X, X[:,0]]
    Xp_closed = c_[Xp, Xp[:,0]]
            
    # Set up the figure
    fig = figure(x_range=axisrange, y_range=axisrange, tools="pan,wheel_zoom,box_zoom,reset,save")
    
    # Set up free hand drawing
    fhdsource = {'x':[], 'y':[]}
    fhdline = fig.multi_line('x', 'y', source=fhdsource)
    fhdtool = FreehandDrawTool(renderers=[fhdline], num_objects=10)
    fig.add_tools(fhdtool)
    pdsource = {'x':[], 'y':[]}
    pdline = fig.multi_line('x', 'y', source=pdsource)
    pdtool = PolyDrawTool(renderers=[pdline], num_objects=10)
    fig.add_tools(pdtool)
    
    # Mark the origin
    fig.cross(0.0, 0.0, size=20, line_color='black', line_width=2.5)

    # The shape before transformation
    fig.line(X_closed[0, :], X_closed[1, :], line_width=2.5, line_color='darkgrey', legend_label='Before')
    fig.circle(X_closed[0, :], X_closed[1, :], size=10, fill_color='darkgrey', line_color='darkgrey')
    for col, label in zip(X.T, ascii_uppercase):
        label_before = Label(x=col[0], y=col[1], x_offset=10, y_offset=10, text=label, text_color='darkgrey', text_font_size="24px")
        fig.add_layout(label_before)

    # The shape after transformation
    fig.line(Xp_closed[0, :], Xp_closed[1, :], line_width=2.5, line_color='red', legend_label='After')
    fig.circle(Xp_closed[0, :], Xp_closed[1, :], size=10, fill_color='red', line_color='red', legend_label='After')
    for col, label in zip(Xp.T, ascii_uppercase):
        label_after = Label(x=col[0], y=col[1], x_offset=10, y_offset=10, text=f"{label}'", text_color='red', text_font_size="24px")
        fig.add_layout(label_after)
        
    return fig